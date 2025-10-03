package com.example.logistica.service;

import com.example.logistica.entity.Conductor;
import com.example.logistica.exception.NotFoundException;
import com.example.logistica.repository.ConductorRepository;
import jakarta.transaction.Transactional;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Transactional
public class ConductorService {

    private final ConductorRepository conductorRepo;

    public Conductor registrarConductor(Conductor c) {
        if (c == null) {
            throw new IllegalArgumentException("El conductor no puede ser nulo");
        }
        return conductorRepo.save(c);
    }

    public ConductorService(ConductorRepository conductorRepo) {
        this.conductorRepo = conductorRepo;
    }

    public List<Conductor> consultarDisponibilidadConductores() {
        return conductorRepo.findByDisponibleTrue();
    }

    public Conductor consultarConductor(Long id) {
        return conductorRepo.findById(id).orElseThrow(() -> new NotFoundException("Conductor no encontrado"));
    }
}
