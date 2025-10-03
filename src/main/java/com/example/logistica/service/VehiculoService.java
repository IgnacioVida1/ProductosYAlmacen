package com.example.logistica.service;

import com.example.logistica.entity.Conductor;
import com.example.logistica.entity.Vehiculo;
import com.example.logistica.exception.NotFoundException;
import com.example.logistica.repository.ConductorRepository;
import com.example.logistica.repository.VehiculoRepository;
import jakarta.transaction.Transactional;
import org.springframework.stereotype.Service;

@Service
@Transactional
public class VehiculoService {

    private final VehiculoRepository vehRepo;
    private final ConductorRepository conductorRepo;

    public VehiculoService(VehiculoRepository vehRepo, ConductorRepository conductorRepo) {
        this.vehRepo = vehRepo;
        this.conductorRepo = conductorRepo;
    }

    public Vehiculo registrarVehiculo(Vehiculo v) {
        if (v == null) {
            throw new IllegalArgumentException("El vehículo no puede ser nulo");
        }
        return vehRepo.save(v);
    }

    public Vehiculo asignarConductorAvehiculo(Long idVehiculo, Long idConductor) {
        Vehiculo v = vehRepo.findById(idVehiculo).orElseThrow(() -> new NotFoundException("Vehículo no encontrado"));
        Conductor c = conductorRepo.findById(idConductor).orElseThrow(() -> new NotFoundException("Conductor no encontrado"));

        v.setIdConductor(idConductor);
        c.setIdVehiculo(idVehiculo);
        c.setDisponible(false);

        conductorRepo.save(c);
        return vehRepo.save(v);
    }

    public Vehiculo consultarVehiculo(Long id) {
        return vehRepo.findById(id).orElseThrow(() -> new NotFoundException("Vehículo no encontrado"));
    }
}
