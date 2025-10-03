package com.example.logistica.service;

import com.example.logistica.entity.AgenteAliado;
import com.example.logistica.exception.NotFoundException;
import com.example.logistica.repository.AgenteAliadoRepository;
import jakarta.transaction.Transactional;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Transactional
public class AgenteAliadoService {

    private final AgenteAliadoRepository agenteRepo;

    public AgenteAliadoService(AgenteAliadoRepository agenteRepo) {
        this.agenteRepo = agenteRepo;
    }


    public AgenteAliado registrarAgente(AgenteAliado agente) {

        if (agente.getIdsConductor() == null) {
            throw new NotFoundException("Agente no encontrado");
        }

        return agenteRepo.save(agente);
    }

    public AgenteAliado asignarAlmacen(Long idAgente, Long idAlmacen) {
        AgenteAliado a = agenteRepo.findById(idAgente).orElseThrow(() -> new NotFoundException("Agente no encontrado"));

        try {
            a.setIdAlmacen(idAlmacen);
        } catch (Error e) {
            throw new IllegalArgumentException("ID de almacén inválido");
        }

        return agenteRepo.save(a);
    }

    public AgenteAliado asignarConductorAagente(Long idAgente, Long idConductor) {
        AgenteAliado a = agenteRepo.findById(idAgente).orElseThrow(() -> new NotFoundException("Agente no encontrado"));
        var list = a.getIdsConductor();
        if (list == null) list = new java.util.ArrayList<>();
        list.add(idConductor);
        a.setIdsConductor(list);
        return agenteRepo.save(a);
    }

    public AgenteAliado consultarAgente(Long id) {
        return agenteRepo.findById(id).orElseThrow(() -> new NotFoundException("Agente no encontrado"));
    }

    public List<AgenteAliado> consultarAgentes() {
        return agenteRepo.findAll();
    }
}
